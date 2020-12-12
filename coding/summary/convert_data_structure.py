def partitionLabels(self, S: str) -> List[int]:
    # find the last position of each char
    last = {c: i for i, c in enumerate(S)}
