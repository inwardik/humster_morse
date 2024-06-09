import subprocess
import time
from dataclasses import dataclass


SIGNAL_DELAY = 0.1
CHAR_DELAY = 1
ADB_ADDR = "c:\\adb\\adb.exe"


@dataclass
class Point:
    x: int
    y: int


class Hamster:
    def __init__(self, text: str, point: Point = Point(550, 1600)) -> None:
        self.text = text
        self.point = point

    def get_code(self, letter: str) -> str:
        morse_mapper = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
        }
        return morse_mapper.get(letter, '')

    def __send_dot(self) -> None:
        subprocess.call(f"{ADB_ADDR} shell input tap {self.point.x} {self.point.y}", shell=True)
        time.sleep(SIGNAL_DELAY)

    def __send_dash(self) -> None:
        subprocess.call(f"{ADB_ADDR}  shell input motionevent DOWN {self.point.x} {self.point.y}", shell=True)
        time.sleep(0.2)
        subprocess.call(f"{ADB_ADDR} shell input motionevent UP {self.point.x} {self.point.y}", shell=True)
        time.sleep(SIGNAL_DELAY)

    def execute(self) -> None:
        for letter in self.text:
            code = self.get_code(letter)
            print(letter, code)
            for item in code:
                if item == '.':
                    self.__send_dot()
                elif item == '-':
                    self.__send_dash()
            time.sleep(CHAR_DELAY)


if __name__ == '__main__':
    hamster = Hamster(input('Enter text: '))
    hamster.execute()
