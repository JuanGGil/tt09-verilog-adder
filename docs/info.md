<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project works by using combinatory logic to add two 4-bit inputs. This is incorporated using Kogge Stone's adder.

## How to test

In test.py assign a value to both dut.a.value and dut.b.value, both values should be at most 15. if the sum is larger than 16, cout will be , otherwise cout is 0. The final sum is dut.sum.value + dut.carry_out.value * 16.

## External hardware

No external hardware was used in this project.
