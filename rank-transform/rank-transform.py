def rank_transform(values: list) -> list:
    """
    Returns the one-based average rank of every value.
    """
    # Write code here

    # we need count of the element in list 
    # and tarting and end index in the sorted list if they are reparting  
    # using the second we can fin the first 

    # we need to know the prev value to campare with
    # we need dict to store the postion 

    # sort the array
    sorted_values = sorted(values)
    rank = {}

    start = 0

    n = len(sorted_values)

    while start < n:
        end = start

        while end < n and  sorted_values[end] == sorted_values[start]:
            end+=1

        avg_value = (start + end + 1) / 2

        rank[sorted_values[start]] = float(avg_value)

        start = end
        
    return [rank[value] for value in values]
            

            
    