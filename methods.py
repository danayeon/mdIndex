def checkSharp(line, n):
    if line[n] == '#':
        return True
    else:
        return False

def generateList(line, n, list='u'):
    if list == 'u':
        sharps = ('#' * n) + ' '
        space = " " * (2 ** (n - 1))
        return space + '-' + space + line.lstrip(sharps)
    elif list == 'o':
        sharps = ('#' * n) + ' '
        space = " " * (2 ** (n - 1))
        return space + '1' + '.' + space + line.lstrip(sharps)
