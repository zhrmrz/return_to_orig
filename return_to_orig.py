from collections import Counter
class Sol:
    def return_to_orig(self,str):
        c=Counter(str)
        if c.get('U')==c.get('D') and c.get('R')==c.get('L'):
            return True
        return False


if __name__ == '__main__':
    p=Sol()
    print(p.return_to_orig('UR'))
