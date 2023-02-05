# 0x05. Processes and signals
An introductory project on:
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

# Requirements
- files are interpreted on Ubuntu 20.04 LTS
- Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
- The first line of all the Bash scripts should be exactly `#!/usr/bin/env bash`

# File Descriptions
## Mandatory
[0-what-is-my-pid](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/0-what-is-my-pid) - a Bash script that displays its own PID

[1-list_your_processes](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/1-list_your_processes) - a Bash script that displays a list of currently running processes
- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

[2-show_your_bash_pid](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/2-show_your_bash_pid) - Bash script that displays lines containing the `bash` word
- cannot use `pgrep`
- The third line of the script must be `# shellcheck disable=SC2009`

[3-show_your_bash_pid_made_easy](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/3-show_your_bash_pid_made_easy) - Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`
- cannot use `ps`

[4-to_infinity_and_beyond](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/4-to_infinity_and_beyond) - a Bash script that displays `To infinity and beyond` indefinitely
- In between each iteration of the loop, add a `sleep 2`

[5-dont_stop_me_now](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/5-dont_stop_me_now) - a Bash script that stops `4-to_infinity_and_beyond` process
- use `kill`

[6-stop_me_if_you_can](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/6-stop_me_if_you_can) - a Bash script that stops `4-to_infinity_and_beyond` process
- use `kill` or `killall`

[7-highlander](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/7-highlander) -  a Bash script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

[8-beheaded_process](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/8-beheaded_process) - a Bash script that kills the process `7-highlander`

## Advanced
[100-process_and_pid_file](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/100-process_and_pid_file) - 
- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?!` when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal


[manage_my_process](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/manage_my_process) Bash script that:
- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

[101-manage_my_process](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/101-manage_my_process) - Bash (init) script that manages `manage_my_process`

**Requirements:**
- When passing the argument `start`:
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process started`
- When passing the argument `stop`:
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Displays `manage_my_process stopped`
- When passing the argument restart
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process` restarted
- Displays Usage: `manage_my_process {start|stop|restart}` if any other argument or no argument is passed

[102-zombie.c](https://github.com/Gbeminiyi-S/alx-system_engineering-devops/tree/master/0x05-processes_and_signals/102-zombie.c)- a C program that creates 5 zombie processes
- For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
- When the code is done creating the parent process and the zombies, use the function below:

```
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
