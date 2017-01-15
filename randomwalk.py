def random_walk(num_steps):
    steps = [(0,0)]
    for i in range(num_steps):
        val = random.randint(0,3)
        if val==0:
            steps.append((steps[-1][0],steps[-1][1]+1))
        elif val==1:
            steps.append((steps[-1][0]+1,steps[-1][1]))
        elif val==2:
            steps.append((steps[-1][0],steps[-1][1]-1))
        elif val==3:
            steps.append((steps[-1][0]-1,steps[-1][1]+1))
    return steps
