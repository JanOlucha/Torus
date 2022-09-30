w = 500
inc = 0
def matrix_Multiplication(matrix,vector): # hard coded to work by multiplying 3x3 matrix with 3x1 vectors ONLY
    result_vector = []
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += matrix[i][j]*vector[j]
        result_vector.append(sum)
    return(result_vector)
    

class object:
    def __init__(self):
        self.point_array = []
        self.light_values = []
        self.divisions = 100
        self.phi_divisions = 30
        self.d_theta = TWO_PI/self.divisions
        self.d_phi = TWO_PI/self.phi_divisions
        self.theta=0
        self.phi=0   
        self.R = 100
        self.r = 50
        
        for i in range(self.divisions): #increasing theta
            self.phi=0
            for j in range(self.phi_divisions): #doing an entire circle rotating phi
                x = self.R*cos(self.theta)+self.r*cos(self.phi)*cos(self.theta)
                y = self.R*sin(self.theta)+self.r*cos(self.phi)*sin(self.theta)
                z = self.r*sin(self.phi)
                self.point_array.append([x,y,z]) #i = x axis, j = y axis, k = z axis
                #self.polar_array.append([self.radius,self.phi,self.theta]) #i = x axis, j = y axis, k = z axis
                self.light_values.append(0) #i = x axis, j = y axis, k = z axis
                #print(self.theta)
                self.phi+=self.d_phi
            self.theta+=self.d_theta
        
            
    def show(self):
        for i in range(len(self.point_array)):
            
            
            hu = map(i,0,len(self.point_array),0,255)
            strokeWeight(3)
            stroke(hu,255,self.light_values[i])
            point(self.point_array[i][0],self.point_array[i][2])
            
    def rota(self,x_angle,y_angle,z_angle): #function to rotate the torus, we use 3D rotation matrices
        x_matrix=[[1,0,0],[0,cos(x_angle),-sin(x_angle)],[0,sin(x_angle),cos(x_angle)]]
        y_matrix=[[cos(y_angle),0,sin(y_angle)],[0,1,0],[-sin(y_angle),0,cos(y_angle)]]
        z_matrix=[[cos(z_angle),-sin(z_angle),0],[sin(z_angle),cos(z_angle),0],[0,0,1]]
        for i in range(len(self.point_array)):
            new_vect = matrix_Multiplication(x_matrix,self.point_array[i])
            new_vect = matrix_Multiplication(y_matrix,new_vect)
            new_vect = matrix_Multiplication(z_matrix,new_vect)
            self.point_array[i]=new_vect
            
    def shadow(self): #still some work to do on the  shadows
        light_vector = [-1,-1,0] #please put in a unit vector
        for i in range(len(self.point_array)):
            x = self.point_array[i][0]
            y = self.point_array[i][1]
            z = self.point_array[i][2]
            normal_x = 2*x*(-self.R+sqrt(pow(x,2)+pow(y,2)))/(sqrt(pow(x,2)+pow(y,2)))
            normal_y = 2*y*(-self.R+sqrt(pow(x,2)+pow(y,2)))/(sqrt(pow(x,2)+pow(y,2)))
            normal_z = 2*z
            dot_product = normal_x*light_vector[0]+normal_y*light_vector[1]+normal_z*light_vector[2]
            normal_mag = sqrt(pow(normal_x,2)+pow(normal_y,2)+pow(normal_z,2))
            self.light_values[i]=map(dot_product,-normal_mag,normal_mag,20,255)
        
            

obj = object()
def setup():
    colorMode(HSB)
    background(0)
    size(600,600,P2D)
    translate(width/2,height/2)
    obj.show()
def draw():
    global inc 
    inc += 2
    background(0)
    translate(width/2,height/2)
    obj.show()
    obj.rota(noise(inc/100)/15,-noise(inc/100)/15,noise(inc/100)/15)

    obj.shadow()

    
