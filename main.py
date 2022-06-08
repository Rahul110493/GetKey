
def getKey(dict, path,  default=None):
    keys = path.split(".")
    val = None

    for key in keys:
        if val:
            if isinstance(val, list):
                val = [v.get(key, default) if v else None for v in val]
            else:
                val = val.get(key, default)
        else:
            val = dict.get(self, key, default)

        if not val:
                break

        return val

if __name__ == '__main__':
    dict = {“a”:{“b”:{“c”:”d”}}}
    path = 'a.b.c'
    print(getKey(dict, path))
