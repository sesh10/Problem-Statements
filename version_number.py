class Solution:
    def compareVersion(self, version1, version2):
        # Fill this in.
        a = [int(x) for x in version1.split('.')]
        b = [int(y) for y in version2.split('.')]
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b.append(0)
        elif len(b) > len(a):
            for i in range(len(b)-len(a)):
                a.append(0)

        for i in range(len(a)):
            if a[i] == b[i]:
                continue
            elif a[i] > b[i]:
                print('version1 > version2')
                return 1
            else:
                print('version2> version1')
                return -1
        return 0
        

version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
