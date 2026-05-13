# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting Up Counter Test")

    # Create clock: 10 us period
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0

    # Wait during reset
    await ClockCycles(dut.clk, 2)

    # Release reset
    dut.rst_n.value = 1

    dut._log.info("Checking counter operation")

    # Counter starts from 1 after first clock edge
    for expected_count in range(1, 17):

        await ClockCycles(dut.clk, 1)

        observed = dut.uo_out.value.integer & 0xF

        expected = expected_count % 16

        dut._log.info(
            f"Expected Count = {expected}, Observed Count = {observed}"
        )

        assert observed == expected, \
            f"Counter mismatch: Expected {expected}, Got {observed}"

    dut._log.info("Up Counter Test Passed")
