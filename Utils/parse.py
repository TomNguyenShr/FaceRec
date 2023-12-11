import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    return(input_path, output_path)
    
