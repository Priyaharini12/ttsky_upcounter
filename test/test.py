import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting Test")

    # Start clock
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initialize
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0

    for _ in range(5):
        await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    for expected in range(1, 16):

        await RisingEdge(dut.clk)

        observed = dut.uo_out.value.integer & 0xF

        dut._log.info(
            f"Expected={expected} Observed={observed}"
        )

        assert observed == expected

    dut._log.info("TEST PASSED")
