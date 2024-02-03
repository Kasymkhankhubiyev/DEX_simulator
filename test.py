from helper import is_float, is_numeric


if __name__ == "__main__":
    try:
        if is_float('0.01'.strip()):
            print('passed')
        else:
            print('Not float')
    except Exception:
        print('failed')