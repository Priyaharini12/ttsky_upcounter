import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting Test")

    # Start clock
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset
    dut.rst_n.value = 0

    # Hold reset for few cycles
    for _ in range(5):
        await RisingEdge(dut.clk)

    # Release reset
    dut.rst_n.value = 1

    # Wait one cycle after reset
    await RisingEdge(dut.clk)

    dut._log.info("Checking counter")

    # Verify counting
    for expected in range(16):

        observed = dut.uo_out.value.to_unsigned() & 0xF

        dut._log.info(
            f"Expected={expected} Observed={observed}"
        )

        assert observed == expected, \
            f"Expected {expected}, Got {observed}"

        await RisingEdge(dut.clk)

    dut._log.info("TEST PASSED")
