def split_sdf(input_file, max_structures_per_file=1):

    # Read the input SDF file

    with open(input_file, 'r') as f:
        sdf_data = f.read().strip().split("$$$$\n")

    # Calculate the number of output files needed

    num_output_files = (len(sdf_data) // max_structures_per_file) + 1

    # Split the sdf data into chunks

    sdf_chunks = [sdf_data[i:i+max_structures_per_file] for i in range(0, len(sdf_data), max_structures_per_file)]

    # Save each chunk into a separate output SDF file

    for i, chunk in enumerate(sdf_chunks):
        output_file = f"output_{i + 1}.sdf"
        with open(output_file, 'w') as f_out:
            f_out.write("".join(chunk))

if __name__ == "__main__":
    input_sdf_file = "/Users/asif/Downloads/ligs.sdf"  # Replace with the name of your large input SDF file
    max_structures_per_file = 1  # Set the desired maximum number of structures per output file
    split_sdf(input_sdf_file, max_structures_per_file)
