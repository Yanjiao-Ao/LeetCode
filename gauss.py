import numpy as np

def gauss(x, y, sigma):
    # Gauss function
    s2 = sigma*sigma
    return 1.0 / np.sqrt(2.0*np.pi*s2) *  np.exp(-(x*x + y*y) / (2.0*s2))

for i in range(0,76):
    sigma = (i + 5)/50
    path = 'gauss_out_'+ str(i) + '.pov'

# setup mesh
    div = 40
    pos = np.zeros([div, div, 3])
    # Write Camera and Light settings
    with open(path, mode='w') as f:
        f.write("camera{" + "\n")
        f.write("\t" + "location <0, -5, 5>" + "\n")
        f.write("\t" + "right <-1.33, 0, 0>" + "\n")
        f.write("\t" + "up <0, 0, 1>" + "\n")
        f.write("\t" + "angle 30" + "\n")
        f.write("\t" + "look_at  <0, 0, 0>" + "\n")
        f.write("}" + "\n")
        f.write("light_source{ <5, -5, 5> color rgb <1, 1, 1> }" + "\n")
        # setup mesh
        for i in range(div):
            for j in range(div):
                # x, y = [-5, +5]
                x = 10.0 * float(i) / float(div-1) - 5.0
                y = 10.0 * float(j) / float(div-1) - 5.0
                # compute z value according to gauss function.
                z = gauss(x, y, sigma)
                pos[i][j] = np.array([x, y, z])

        # Write Object as mesh
        f.write("object{" + "\n")
        f.write("\tmesh{" + "\n")

        #Write triangles
        for i in range(div-1): # loop for x
            for j in range(div-1): # loop for y
                p0 = pos[(i + 0), (j + 0)]
                p1 = pos[(i + 1), (j + 0)]
                p2 = pos[(i + 0), (j + 1)]
                p3 = pos[(i + 1), (j + 1)]

                #Write 2 triangles (0, 1, 3) and (0, 3, 2)
                f.write("\t" + "triangle{")
                f.write("<" + str(p0[0]) + "," + str(p0[1]) + "," + str(p0[2]) + ">,")
                f.write("<" + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]) + ">,")
                f.write("<" + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]) + ">}\n")

                f.write("\t" + "triangle{")
                f.write("<" + str(p0[0]) + "," + str(p0[1]) + "," + str(p0[2]) + ">,")
                f.write("<" + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]) + ">,")
                f.write("<" + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]) + ">}\n")

        f.write("\t" + "}" + "\n")
        f.write("\t" +"pigment{ color <0, 1, 0> }" + "\n")
        f.write("\t" +"finish{ diffuse 1.0 ambient 0.0 }" + "\n")
        f.write("}" + "\n")

