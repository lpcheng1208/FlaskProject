# from time import time, sleep
#
#
# def time_dec(func):
#     def decorate(*args, **kwargs):
#         before = time()
#         func(*args, **kwargs)
#         after = time()
#
#         print(after - before)
#
#     return decorate
#
#
# @time_dec
# def play():
#     sleep(4)
#
#     print("我的LOL瞎子特别厉害")
#
#
# @time_dec
# def run():
#     sleep(3)
#
#     print("我的跑步特别快")
#
#
# if __name__ == '__main__':
#     play()
#     run()

class Solution:
    def replaceSpace(self, s):
        m = s.replace(" ", "%20")

        print(m)


sou = Solution()
sou.replaceSpace("hello world")
