import argparse


def argument_list():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=str, help="File prefix")
    parser.add_argument("-i", "--input", default="", type=str, help="Input file for matrices")
    parser.add_argument("-n", "--n_pops", required=True, type=int, help="Number of populations")
    parser.add_argument("-s", "--sample_size", required=True, type=int, help="Sample size of the populations")
    parser.add_argument("-g", "--growth_rate", default=0, type=int, help="Growth rates of the populations")
    parser.add_argument("-m", "--mutation_rate", required=True, type=str, help="Mutation")
    args = parser.parse_args()

    return args


def create_tpl(arguments):
    output_file = arguments.file + ".tpl"
    with open(output_file, "w") as f:
        f.write(f"//Number of population samples (demes)\n")
        f.write(f"{arguments.n_pops} populations to simulate\n")

        f.write(f"//Population effective sizes (number of genes)\n")
        for i in range(arguments.n_pops):
            f.write(f"N_POP{i}\n")

        f.write(f"//Sample sizes\n")
        for i in range(arguments.n_pops):
            f.write(f"{arguments.sample_size}\n")

        f.write(f"//Growth rates\n")
        for i in range(arguments.n_pops):
            f.write(f"{arguments.growth_rate}\n")

        f.write(f"//Number of migration matrices\n")
        f.write(f"{arguments.n_pops}\n")

        if arguments.input == "":
            for i in range(arguments.n_pops):
                f.write(f"//Migration matrix {i}\n")
                for j in range(arguments.n_pops):
                    for k in range(arguments.n_pops):
                        f.write(f"0.000 ")
                    f.write(f"\n")
        else:
            with open(arguments.input, "r") as input_f:
                for line in input_f:
                    f.write(f"{line}")



#def create_est(argument):




def main():
    arg_list = argument_list()

    create_tpl(arg_list)
    #create_est(arg_list)


if __name__ == "__main__":
    main()