
def main():
    import argparse
    import logging
    from humanfriendly import parse_size
    from nagcpy import nix_heuristic_gc

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--penalize-drvs", default=True, action=argparse.BooleanOptionalAction)
    parser.add_argument("--penalize-substitutable", default=True, action=argparse.BooleanOptionalAction)
    parser.add_argument("--penalize-inodes", default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument("--dry-run", default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument("reclaim_bytes")

    parsed = vars(parser.parse_args())

    parsed["reclaim_bytes"] = parse_size(parsed["reclaim_bytes"])

    nix_heuristic_gc(**parsed)

if __name__ == "__main__":
    main()
