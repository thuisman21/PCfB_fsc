import argparse


def argument_list():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--n_pops", required=True, type=int, help="Number of populations")
    parser.add_argument("-s", "--sample_size", required=True, type=int, help="Sample size of the populations")
    parser.add_argument("-g", "--growth_rate", default=0, type=int, help="Growth rates of the populations")
    parser.add_argument("-m", "--mutation_rate", required=True, type=str, help="Mutation")
    args = parser.parse_args()

    return args


def main():
    arg_list = argument_list()


if __name__ == "__main__":
    main()