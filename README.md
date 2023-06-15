# pop3-fuzzer

This fuzzer is a script created to probe and study concepts of buffer overflow, initially specific for exploit old pop3 servers. It consists basically in send fuzzed data to the mail server, and try to execute a buffer overflow by fill the entire memory stack.

Run normally:

```bash
    git clone https://github.com/Aleffelisberto/pop3-fuzzer.git
    cd pop3-fuzzer

    # Your can run it like a script
    chmod +x fuzzer.py
    ./fuzzer.py

    # Or you can run it using python 3
    python3 fuzzer.py
```

Usage:

```
    positional arguments: host

    options:
    -h, --help            show this help message and exit
    -p PORT, --port PORT  Port to establish connection. Default port is 110
    -u USERNAME, --username USERNAME
    -f FUZZ_PATTERN, --fuzz_pattern FUZZ_PATTERN
                            Fuzzing pattern to fill buffer. Default is 'A'
    -o OFFSET, --offset OFFSET
                            Offset used to build buffer. Default is 50
    -l LENGTH, --length LENGTH
                            Size of the buffer (i.e. amount of attempts based on how many words are stored).
                            Default is 30
    -t TIME_SLEEP, --time_sleep TIME_SLEEP
                            Sleep time (in seconds) to use between each request. Default is 1
```
