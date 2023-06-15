#!/usr/bin/python3
# fuzzer.py v1

import socket
from time import sleep
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("-p", "--port", type=int, default=110, choices=range(0, 65535),
                        help="Port to establish connection. Default port is 110")
    parser.add_argument("-u", "--username", type=str, default="admin")
    parser.add_argument("-f", "--fuzz_pattern", type=str, default="A",
                        help="Fuzzing pattern to fill buffer. Default is 'A'")
    parser.add_argument("-o", "--offset", type=int, default=50, choices=range(1, 50),
                        help="Offset used to build buffer. Default is 50")
    parser.add_argument("-l", "--length", type=int, default=30, choices=range(1, 30),
                        help="Size of the buffer (i.e. amount of attempts based on how many words are stored). Default is 30")
    parser.add_argument("-t", "--time_sleep", type=int, default=1,
                        help="Sleep time (in seconds) to use between each request. Default is 1")
    args = parser.parse_args()
    return args


def create_buffer(ch: str, length: int, offset: int) -> list[str]:
    buffer = [ch]
    while len(buffer) <= length:
        print(buffer)
        buffer.append(ch * offset)
        offset += offset
    return buffer


def fuzz(buffer: list[str], host: str, username: str, port: int = 110, sleep_time: int = 1) -> None:
    for word in buffer:
        print(f"Fuzzind PASSWORD with {len(word)} bytes")
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((host, port))
        tcp_socket.recv(1024)
        tcp_socket.send(f"USER {username}\r\n")
        sleep(sleep_time)
        tcp_socket.recv(1024)
        tcp_socket.send(f"PASS {word}\r\n")
        sleep(sleep_time)
        tcp_socket.send("QUIT\r\n")
        tcp_socket.close()


def main():
    args = parse_arguments()
    buffer = create_buffer(args.fuzz_pattern, args.length, args.offset)
    fuzz(buffer, args.host, args.username, args.time_sleep)


if __name__ == "__main__":
    main()
