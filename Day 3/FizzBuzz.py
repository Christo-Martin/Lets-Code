class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1, n + 1):
            if not i % 15:
                a += ["FizzBuzz"]
            elif not i % 5:
                a += ["Buzz"]
            elif not i % 3:
                a += ["Fizz"]
            else:
                a += [str(i)]
        return a