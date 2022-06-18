class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.flip_set = [1] * size
        self.bit_count = 0

    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.bitset[idx] = 1
            self.flip_set[idx] = 0
            self.bit_count += 1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx]:
            self.bitset[idx] = 0
            self.flip_set[idx] = 1
            self.bit_count -= 1

    def flip(self) -> None:
        self.bitset, self.flip_set = self.flip_set, self.bitset
        self.bit_count = len(self.bitset) - self.bit_count

    def all(self) -> bool:
        return self.bit_count == len(self.bitset)

    def one(self) -> bool:
        return self.bit_count > 0

    def count(self) -> int:
        return self.bit_count

    def toString(self) -> str:
        return ''.join(str(each) for each in self.bitset)
