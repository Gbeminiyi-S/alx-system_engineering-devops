# 0x04. Loops, conditions and parsing
An introductory project on:

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

# Requirements
- files are interpreted on Ubuntu 20.04 LTS
- Bash script must pass `Shellcheck` (version `0.7.0`) without any error
- The first line of all the Bash scripts should be exactly `#!/usr/bin/env bash`

# File Descriptions
## Mandatory
[0-RSA_public_key.pub](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub) - Create a SSH RSA key pair

[1-for_best_school](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/1-for_best_school) - a Bash script that displays `Best School` 10 times, using `for` loop

[2-while_best_school](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/2-while_best_school) - a Bash script that displays `Best School` 10 times, using `while` loop

[3-until_best_school](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/3-until_best_school) -  a Bash script that displays `Best School` 10 times, using `until` loop

[4-if_9_say_hi](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/4-if_9_say_hi) - a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line. 
- Use a `while` loop and `if` statement

[5-4_bad_luck_8_is_your_chance](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance) - a Bash script that loops from 1 to 10 and:
- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for the other iterations
- Use a `while loop` and `if`,`elif` and `else` statements

[6-superstitious_numbers](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/6-superstitious_numbers) - a Bash script that displays numbers from 1 to 20 and:
- displays `4` and then `bad luck from China` for the 4th loop iteration
- displays `9` and then `bad luck from Japan` for the 9th loop iteration
- displays `17` and then `bad luck from Italy` for the 17th loop iteration
- Use a `while loop` and `case` statement

[7-clock](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/7-clock) - a Bash script that displays the time for 12 hours and 59 minutes:
- display hours from 0 to 12
- display minutes from 1 to 59
- Use a `while loop`

[8-for_ls](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/8-for_ls) - a Bash script that displays:
- The content of the current directory
- In a list format
- Where only the part of the name after the first dash is displayed
- Use a `for` loop
- Do not display hidden files
