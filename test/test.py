# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting Up Counter Test")

    # Create 10 us clock period
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply active-low reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # Release reset
    dut.rst_n.value = 1

    dut._log.info("Checking counter operation")

    # Check counter values
    for expected_count in range(16):

        await ClockCycles(dut.clk, 1)

        observed = dut.uo_out.value.integer & 0xF

        dut._log.info(
            f"Expected Count = {expected_count}, Observed Count = {observed}"
        )

        assert observed == expected_count, \
            f"Counter mismatch: Expected {expected_count}, Got {observed}"

    dut._log.info("Up Counter Test Passed")
