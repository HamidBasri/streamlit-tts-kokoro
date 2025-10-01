def quality_color(overall):
    if overall in ["A", "A-"]:
        return "#4CAF50"  # Green
    elif overall in ["B", "B-", "C+"]:
        return "#FFEB3B"  # Yellow
    elif overall in ["C", "C-"]:
        return "#FF9800"  # Orange
    elif overall in ["D", "D-", "F", "F+"]:
        return "#F44336"  # Red
    else:
        return "#9E9E9E"  # Grey for N/A
