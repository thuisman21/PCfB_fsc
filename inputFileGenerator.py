import argparse


def argument_list():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=str, help="output files prefix")
    parser.add_argument("-i", "--input", default="", type=str, help="input file for matrices")
    parser.add_argument("-n", "--n_pops", required=True, type=int, help="Number of populations")
    parser.add_argument("-s", "--sample_size", required=True, type=int, help="sample size of the populations")
    parser.add_argument("-g", "--growth_rate", default=0, type=int, help="growth rates of the populations")
    parser.add_argument("-m", "--mutation_rate", required=True, type=str, help="mutation rate")
    parser.add_argument("-e", "--events", required=True, type=str, help="historical events the model is based on")
    parser.add_argument("-l", "--loci", default=1, type=int, help="number of loci")
    parser.add_argument("-b", "--blocks", default=1, type=int, help="number of linkage blocks ")
    args = parser.parse_args()

    return args


def create_tpl(arguments):
    output_tpl = arguments.file + ".tpl"
    with open(output_tpl, "w") as f:
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
            f.write(f"\n")

        f.write(f"//historical event: time, source, sink, migrants, new deme size, growth rate, migr mat index\n")
        with open(arguments.events, "r") as events_f:
            for line in events_f:
                f.write(f"{line}")
            f.write(f"\n")

        f.write(f"//Number of independent loci [chromosomes]\n")
        f.write(f"{arguments.loci} 0\n")

        f.write(f"//Per chromosome: Number of linkage blocks\n")
        f.write(f"{arguments.blocks}\n")

        f.write(f"//per block: Datatype, numm loci, rec rate and mut rate + optional parameters\n")
        f.write(f"FREQ {arguments.loci} 0 {arguments.mutation_rate} OUTEXP")


def create_est(arguments):
    output_est = arguments.file + ".est"
    with open(output_est, "w") as f:
        f.write(f"// Priors and rules file\n")
        f.write(f"// *********************\n")

        f.write(f"\n[PARAMETERS]\n")
        f.write(f"//#isInt? #name   #dist.#min  #max\n")
        f.write(f"//all Ns are in number of haploid individuals\n")


def main():
    arg_list = argument_list()

    print(f"Creating first input file {arg_list.file}.tpl")
    create_tpl(arg_list)
    print(f"{arg_list.file}.tpl created, with {arg_list.n_pops} populations and sample sizes of {arg_list.sample_size}.")

    print(f"Creating second input file {arg_list.file}.est")
    create_est(arg_list)
    print(f"{arg_list.file}.est created.")


if __name__ == "__main__":
    main()