import math

def main():

    class Rectangle:
        def __init__(self, width: int, height: int) -> None:
            self.width = width
            self.height = height
        
        def set_width(self, width: int) -> None:
            self.width = width

        def set_height(self, height: int) -> None:
            self.height = height

        def get_area(self) -> int:
            return self.width * self.height
        
        def get_perimeter(self) -> int:
            return 2 * (self.width + self.height)

        def get_diagonal(self) -> int:
            return math.sqrt(self.width ** 2 + self.height ** 2)
        
        def get_picture(self) -> str:
            if self.width > 50 or self.height > 50:
                return "Too big for picture."
            
            result = ""

            for height in range(self.height):
                result += '*' * self.width
                result += '\n'
            
            return(result)
        
        def get_amount_inside(self, rectangle: "Rectangle") -> int:
            return math.floor(self.get_area() / rectangle.get_area())

        def __str__(self) -> str:
            return f'Rectangle(width={self.width}, height={self.height})'
        
    class Square(Rectangle):
        def __init__(self, size: int) -> None:
            super().__init__(size, size)
        
        def set_width(self, size: int) -> None:
            self.width = size
            self.height = size

        def set_height(self, size: int) -> None:
            self.width = size
            self.height = size

        def set_side(self, size: int) -> None:
            self.set_width(size)
            self.set_height(size)
        
        def __str__(self) -> str:
            return f'Square(side={self.width})'

    # ------------------------------
    # Example code
    # ------------------------------
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

    # ------------------------------
    # Expected result
    #
    # 50
    # 26
    # Rectangle(width=10, height=3)
    # **********
    # **********
    # **********
    #   
    # 81
    # 5.656854249492381
    # Square(side=4)
    # ****
    # ****
    # ****
    # ****
    #
    # 8
    # ------------------------------

if __name__ == "__main__":
    main()