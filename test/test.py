# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.a.value = 13
    dut.b.value = 10

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 10)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 1
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 0 

    # test 2
    dut.a.value = 1
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 0 

    # test 3
    dut.a.value = 0
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 0 

    # test 4
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0 

    # test 5
    dut.a.value = 2
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0 

    # test 6
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0 

    # test 7
    dut.a.value = 2
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0 

    # test 8
    dut.a.value = 1
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0 

    # test 9
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0 

    # test 10
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0 

    # test 11
    dut.a.value = 0
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0 

    # test 12
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0 

    # test 13
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0 

    # test 14
    dut.a.value = 3
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 15
    dut.a.value = 2
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 16
    dut.a.value = 3
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 17
    dut.a.value = 4
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0 

    # test 18
    dut.a.value = 0
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0 

    # test 19
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 20
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 21
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 22
    dut.a.value = 2
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 23
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 24
    dut.a.value = 3
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 25
    dut.a.value = 4
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 26
    dut.a.value = 5
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 27
    dut.a.value = 0
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0 

    # test 28
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 29
    dut.a.value = 1
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 30
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 31
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 32
    dut.a.value = 5
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 33
    dut.a.value = 3
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 34
    dut.a.value = 5
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 35
    dut.a.value = 4
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 36
    dut.a.value = 5
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 37
    dut.a.value = 6
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 38
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0 

    # test 39
    dut.a.value = 6
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 40
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 41
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 42
    dut.a.value = 2
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 43
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 44
    dut.a.value = 3
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 45
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 46
    dut.a.value = 4
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 47
    dut.a.value = 6
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 48
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 49
    dut.a.value = 6
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 50
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 51
    dut.a.value = 0
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0 

    # test 52
    dut.a.value = 7
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 53
    dut.a.value = 1
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 54
    dut.a.value = 7
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 55
    dut.a.value = 2
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 56
    dut.a.value = 7
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 57
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 58
    dut.a.value = 7
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 59
    dut.a.value = 4
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 60
    dut.a.value = 7
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 61
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 62
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 63
    dut.a.value = 6
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 64
    dut.a.value = 7
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 65
    dut.a.value = 8
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 66
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0 

    # test 67
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 68
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 69
    dut.a.value = 8
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 70
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 71
    dut.a.value = 8
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 72
    dut.a.value = 3
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 73
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 74
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 75
    dut.a.value = 8
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 76
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 77
    dut.a.value = 8
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 78
    dut.a.value = 6
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 79
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 80
    dut.a.value = 7
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 81
    dut.a.value = 8
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 82
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 83
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0 

    # test 84
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 85
    dut.a.value = 1
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 86
    dut.a.value = 9
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 87
    dut.a.value = 2
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 88
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 89
    dut.a.value = 3
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 90
    dut.a.value = 9
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 91
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 92
    dut.a.value = 9
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 93
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 94
    dut.a.value = 9
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 95
    dut.a.value = 6
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 96
    dut.a.value = 9
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1

    # test 97
    dut.a.value = 7
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 98
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 99
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 100
    dut.a.value = 9
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1

    # test 101
    dut.a.value = 10
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 102
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0 

    # test 103
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 104
    dut.a.value = 1
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 105
    dut.a.value = 10
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 106
    dut.a.value = 2
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 107
    dut.a.value = 10
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 108
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 109
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 110
    dut.a.value = 4
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 111
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 112
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 113
    dut.a.value = 10
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 114
    dut.a.value = 6
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1

    # test 115
    dut.a.value = 10
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 116
    dut.a.value = 7
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1

    # test 117
    dut.a.value = 10
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 118
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 119
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1

    # test 120
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1

    # test 121
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 122
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 123
    dut.a.value = 0
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0 

    # test 124
    dut.a.value = 11
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 125
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 126
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 127
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 128
    dut.a.value = 11
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 129
    dut.a.value = 3
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 130
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 131
    dut.a.value = 4
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 132
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 133
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 134
    dut.a.value = 11
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1

    # test 135
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 136
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 137
    dut.a.value = 7
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 138
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 139
    dut.a.value = 8
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 140
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1

    # test 141
    dut.a.value = 9
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 142
    dut.a.value = 11
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 143
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 144
    dut.a.value = 11
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 145
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 146
    dut.a.value = 0
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0 

    # test 147
    dut.a.value = 12
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 148
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 149
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 150
    dut.a.value = 2
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 151
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 152
    dut.a.value = 3
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 153
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1

    # test 154
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 155
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 156
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 157
    dut.a.value = 12
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 158
    dut.a.value = 6
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 159
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 160
    dut.a.value = 7
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1

    # test 161
    dut.a.value = 12
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 162
    dut.a.value = 8
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 163
    dut.a.value = 12
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 164
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1

    # test 165
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 166
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 167
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 168
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 169
    dut.a.value = 12
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 170
    dut.a.value = 13
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 171
    dut.a.value = 0
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0 

    # test 172
    dut.a.value = 13
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 173
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 174
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 175
    dut.a.value = 2
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 176
    dut.a.value = 13
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 177
    dut.a.value = 3
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 178
    dut.a.value = 13
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 179
    dut.a.value = 4
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 180
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1

    # test 181
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 182
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 183
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 184
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 185
    dut.a.value = 7
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 186
    dut.a.value = 13
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 187
    dut.a.value = 8
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 188
    dut.a.value = 13
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 189
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 190
    dut.a.value = 13
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 191
    dut.a.value = 10
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 192
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 193
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 194
    dut.a.value = 13
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1 

    # test 195
    dut.a.value = 12
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1 

    # test 196
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1 

    # test 197
    dut.a.value = 14
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 198
    dut.a.value = 0
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0 

    # test 199
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 200
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 201
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 202
    dut.a.value = 2
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 203
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 204
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 205
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 206
    dut.a.value = 4
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 207
    dut.a.value = 14
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 208
    dut.a.value = 5
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 209
    dut.a.value = 14
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 210
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 211
    dut.a.value = 14
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 212
    dut.a.value = 7
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 213
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 214
    dut.a.value = 8
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 215
    dut.a.value = 14
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 216
    dut.a.value = 9
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 217
    dut.a.value = 14
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 218
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 219
    dut.a.value = 14
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1 

    # test 220
    dut.a.value = 11
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1 

    # test 221
    dut.a.value = 14
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1

    # test 222
    dut.a.value = 12
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1 

    # test 223
    dut.a.value = 14
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1 

    # test 224
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1

    # test 225
    dut.a.value = 14
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1 

    # test 226
    dut.a.value = 15
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 227
    dut.a.value = 0
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0 

    # test 228
    dut.a.value = 15
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1

    # test 229
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1 

    # test 230
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 231
    dut.a.value = 2
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1 

    # test 232
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 233
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1 

    # test 234
    dut.a.value = 15
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 235
    dut.a.value = 4
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1 

    # test 236
    dut.a.value = 15
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 237
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1 

    # test 238
    dut.a.value = 15
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 239
    dut.a.value = 6
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1 

    # test 240
    dut.a.value = 15
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 241
    dut.a.value = 7
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1 

    # test 242
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 243
    dut.a.value = 8
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # test 244
    dut.a.value = 15
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 245
    dut.a.value = 9
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1 

    # test 246
    dut.a.value = 15
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1

    # test 247
    dut.a.value = 10
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1 

    # test 248
    dut.a.value = 15
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1

    # test 249
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1 

    # test 250
    dut.a.value = 15
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1 

    # test 251
    dut.a.value = 12
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1 

    # test 252
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1 

    # test 253
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1 

    # test 254
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1 

    # test 255
    dut.a.value = 14
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1 

    # test 256
    dut.a.value = 15
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 1

    # TESTING MINIMUM CLOCK CYCLES FOR VARYING NUMBERS

    # test 257
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 1)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}. 1 Clock Cycles")
    assert dut.sum.value == 0 and dut.carry_out.value == 0 

    # test 258
    dut.a.value = 15
    dut.b.value = 15
    await ClockCycles(dut.clk, 1)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}. 1 Clock Cycles")
    assert dut.sum.value == 14 and dut.carry_out.value == 1 

    # test 259
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 1)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}. 1 Clock Cycles")
    assert dut.sum.value == 0 and dut.carry_out.value == 0 

    # test 260
    dut.a.value = 15
    dut.b.value = 15
    await ClockCycles(dut.clk, 1)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}. 1 Clock Cycles")
    assert dut.sum.value == 14 and dut.carry_out.value == 1 

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    
