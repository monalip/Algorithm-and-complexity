import sys
import os
from termios import tcflush, TCIFLUSH

def getInput():
	#tcflush(sys.stdin, TCIFLUSH)
	lines = []
	for line in sys.stdin:
		lines.append(line)
	return lines


def accessInstance(lines):
    roles = lines[0]  # No.of roles
    vertices = int(roles)
    scenes = lines[1]  # No.of scenes
    edges = int(scenes)
    actors = lines[2]  # No.of actors
    colors = int(actors)

    edgeDetails = []
    for i in range(3, (len(lines))):
        edgeDetails.append(lines[i])
    return vertices, edges, colors, edgeDetails


def vertexColoring(vertices, edges, colors, edgeDetails):
    vertexColoringFlag = True
    edgeMatrix = edgeMatrixConstruct(vertices, edgeDetails)
    vertexColor = np.ones(shape=(vertices, colors), dtype=int)
    while (vertexColoringFlag == True):
        # TODO: Make vertex allocation coloring easy.
        vertexColor, coloringNeed = allocVertexColors(edgeMatrix, vertices, colors, vertexColor)
        if not coloringNeed:
            vertexColoringFlag = False
        print(vertexColor)


def edgeMatrixConstruct(vertices, edgeDetails):
    edgeMatrix = np.zeros(shape=(vertices, vertices), dtype=int)
    for eachEdgeConnection in edgeDetails:
        index = []
        for eachVal in eachEdgeConnection:
            index.append(eachVal)
        index1 = int(index[0])
        index2 = int(index[2])  # Index[1] is an empty string and so it has been skipped.
        edgeMatrix[(index1 - 1), (index2 - 1)] = 1
        edgeMatrix[(index2 - 1), (index1 - 1)] = 1
    return edgeMatrix


def allocVertexColors(edgeMatrix, vertices, colors, vertexColor):
    print(vertexColor)

    ## Step 3: Update colors on each vertices.
    for vertex in range(vertices - 1):
        if (vertex == 0):
            # Assign a random color. Update other colors to zero.
            vertexColor[0][1] = 0
            vertexColor[0][2] = 0
        indexCounter = 0
        indexToBeMapped = []

        for eachVal in edgeMatrix[vertex]:
            if (eachVal == 1):
                indexToBeMapped.append(indexCounter)
            indexCounter += 1

            ## Update vertexColor based on edge connections.
            for val in indexToBeMapped:
                vertexColor[val][vertex] = 0
    print("Now")
    print(vertexColor)

    ## Check whether all rows have only one color. (Each vertex should have only one color).
    verticesNeedAll = []
    vertexIndex = 0
    for val in vertexColor:
        rowCount = 0
        for eachVal in val:
            if (eachVal == 1):
                rowCount += 1
        if (rowCount > 1):
            verticesNeedAll.append(vertexIndex)
        vertexIndex += 1
    print("Now... ")
    verticesNeedAll = []
    return vertexColor, verticesNeedAll


def dispRoles(actor, roles):
    for j in range(roles):
        print(actor," ".join(str(x) for x in range(2,actor+2)))
    dispDefaultRoles(actor)


def dispDefaultRoles(actor):
    print("1 1")
    print("1 2")
    #print(actor," ".join(str(x) for x in range(3,actor+3)))
    print("1 3")
 


def dispDefaultScenes(role,is_v):
    p = int(role) + 1
    q = int(role) + 2
    r = int(role) + 3
    j = 2
    #k = 2 + len(is_v)
    print(j,p,r)
    #print(k, p, r,*is_v, sep=' ')
    print(j, q, r)
    for i in is_v:
    	print(j,i,r)


def dispScenes(edgeConnections, edge,roles,iso_ver):
    for eachVal in edgeConnections:
        eachValue = eachVal.split(' ')
        eachValue[0] = int(eachValue[0])
        eachValue[1] = int(eachValue[1])
        print("2", eachValue[0], eachValue[1])
    dispDefaultScenes(roles,iso_ver)


def reduction1(actors, roles, edgeConnections):
    edgeMatrix = edgeMatrixConstruct(roles, edgeConnections)
    allocDivas(actors, roles, edgeMatrix)


def allocDivas(Act, rol, edgeMat):
    # Assign an actor 1 for vertex 1
    role1 = 1

    ## Assign an actor 2 for an isolated vertex/


def findisolated_vertex(role, edge_list):
    isolate = []
    is_vertex = []
    for val in edge_list:
        eachValue = val.split(' ')
        #print(eachValue)
        a = int(eachValue[0])
        b = int(eachValue[1])
        isolate.append(a)
        isolate.append(b)
    for r in range(1,role+1):
        if r not in isolate:
            is_vertex.append(r)
    return is_vertex

instance = getInput()
V, E, C, EL = accessInstance(instance)
if(C > V):
    print(3,2,3)
    print(3,1,2,3)
    print(3,1,2,3)
    print(3,1,2,3)
    print(2,1,3)
    print(2,2,3)
else:
    IV=findisolated_vertex(V, EL)
    V = V + 3
    E = E + 2
    C = C + 2
    if(C < 3):
        V=3
        C=3
    scene = E - 2
    E = E + len(IV)
    print(V)
    print(E)
    print(C)
    dispRoles(C-2, V-3)
    dispScenes(EL, E-2,V-3,IV)
    os.system('clear') 
    # print(IV)
    # vertexColoring(V, E, C, EL)
    # reduction1(C, V, EL)
# your code goes here# your code goes here# your code goes here# your code goes here