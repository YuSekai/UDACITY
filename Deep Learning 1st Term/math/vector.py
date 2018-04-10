#!/usr/bin/python
# -*- coding: utf-8 -*-

# coding = utf-8
from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30





class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalized the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two three-dimensions'


#初始化并定义函数coordinates 即坐标函数
    def __init__(self,coordinates):

        try:
            if not coordinates:  #若coo函数为空
                raise ValueError  #则显示valueError
            # 定义元组tuple并将coordinates的元素赋值给self.coordinates
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            #将coo的长度赋值给dimension
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise ValueError("The coordinates must be an iterable")
    #定义函数类str，类型为数值，使用str()可将类型变为字符
    def __str__(self):
        #将coo中的值放入格式{}中，print时调用 这里会返回Vector:{1,2,3}替换直接输出1，2，3
            return 'Vector:{}'.format(self.coordinates)
#定义比较类eq ，判断self和v是否相等
    def __eq__(self, v):
            return self.coordinates == v.coordinates
#定义向量加法 plus ，将向量self和v中的值依次相加 x1+y1,x2+y2
     # v + w
    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
v = Vector(['-7.579','-7.88'])
w = Vector(['22.737','23.64'])
print v.plus(w)




    # v - w
    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


#data float
    def times_scalar(self,c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

# x^2+y^2  z
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

# 1/x
    @property
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/Decimal(magnitude))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

#  v.w
    def dot(self,v,tolerance=1e-10):
        dot = sum([x * y for x, y in zip(self.coordinates, v.coordinates)])
        if (abs(dot) > 1) and (abs(dot) - 1 < tolerance):
            if dot > 0:
                dot = 1
            elif dot < 0:
                dot = -1
        return dot

            #check orthogonal vLLw
    def is_orthogonal_to(self,v,tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

# check 0
    def is_zero(self,tolerance=1e-10):

        return self.magnitude() < tolerance

#check parallel  v//w
    def is_parallels_to(self, v):
        return ( self.is_zero() or
                 v.is_zero() or
                 self.angle_with(v) == 0 or
                 self.angle_with(v) == pi )


#  arccos
    def angle_with(self,v,in_degrees = False):
        # type: (object, object) -> object
        try:
            u1 = self.normalized
            u2 = v.normalized
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degress_per_radian = 180. / pi
                return angle_in_radians * degress_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e


    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    def cross(self, v):
        try:
            if self.dimension == 3 and v.dimension == 3:
                x_1, y_1, z_1 = self.coordinates
                x_2, y_2, z_2 = v.coordinates
                new_coordinates = [ y_1*z_2 - y_2*z_1,
                                    -(x_1*z_2 - x_2*z_1),
                                    x_1*y_2 - x_2*y_1 ]
                return Vector(new_coordinates)
            elif self.dimension == 2 and v.dimension == 2:
                raise ValueError('need more than 2 values to unpack')
            elif self.dimension > 3 or v.dimension > 3:
                raise ValueError('too many values to unpack')
            elif self.dimension == 1 or v.dimension == 1:
                raise ValueError('need more than 1 value to unpack')
            elif self.dimension != v.dimension:
                raise ValueError('need two three-dimensional vectors')
            else:
                raise ValueError

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack' or msg == 'need two three-dimensional vectors':
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()

    def area_of_triangle_with(self, v):
        return Decimal(self.area_of_parallelogram_with(v)) / Decimal('2.0')




print 'first pair...'
v = Vector(['-7.579','-7.88'])
w = Vector(['22.737','23.64'])
print v.is_parallels_to(w)
print v.is_orthogonal_to(w)



