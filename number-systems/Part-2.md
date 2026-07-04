Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: It can be written where only one bit is represented as a 1. E.g. 1000000 or 0010000

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: 0x21 is a hexadecimal number which is 33 in decimal, which corresponds to "!" as an ASCII character

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: In greyscale we represent the light intensity (whiteness) by a number between 0 - 255 in decimal (00 and FF in hexadecimal). A value of 0x21 would equal 33 in decimal which is close to black (approx. 1/8 of the way from black to white)

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0, 255

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: This colour would be 10/15 saturated with red, no green and fully saturated with blue. This would likely be an purple colour.
