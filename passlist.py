from itertools import product, combinations, permutations
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--mode', help='mode : single or multi')
parser.add_argument('-w', nargs='+', action='store', help='add a char')
parser.add_argument('-o', help='set a file name output')
parser.add_argument('-l', help='count of range of password', type=int)
parser.add_argument('-t', help='search target')

args = parser.parse_args()


if args.mode == 'single':

    final_passlist = []

    if args.w:
        passlist_obj = permutations(args.w, args.l)
        for i in passlist_obj:
            passlist_target = (''.join(list(map(str, i))))
            final_passlist.append(passlist_target + '\n')

        final_passlist.insert(0, f"count : {len(final_passlist)}\n")

        with open(args.o, mode="w") as f:
            f.writelines(final_passlist)

elif args.mode == 'multi':
    final_passlist = []

    if args.l:
        passlist_obj = product(args.w, repeat=args.l)

        for i in passlist_obj:
            passlist_target = (''.join(list(map(str, i))))
            final_passlist.append(passlist_target + '\n')

        final_passlist.insert(0, f"count : {len(final_passlist)}\n")
        with open(args.o, mode="w") as f:
            f.writelines(final_passlist)

elif args.mode == 'search':
    final_passlist = []
    target = []

    if args.l:
        passlist_obj = product(args.w, repeat=args.l)

        for i in passlist_obj:
            passlist_target = (''.join(list(map(str, i))))
            target.append(passlist_target)
            if passlist_target == args.t:
                raise Exception(f"{target.index(passlist_target) + 1} : {passlist_target} " + '\n')
            final_passlist.append(passlist_target + '\n')

        final_passlist.insert(0, f"count : {len(final_passlist)}\n")
        with open(args.o, mode="w") as f:
            f.writelines(final_passlist)
else:
    raise ValueError("its best password list generator 1 migi na bro negah kon")
