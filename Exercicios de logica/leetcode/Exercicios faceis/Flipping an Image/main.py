class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image_reverse = [list(reversed(img)) for img in image]

        image_invert = []
        for img in image_reverse:
            bits = []
            for bit in img:
                if bit == 0:
                    bits.append(1)
                    continue
                bits.append(0)
            image_invert.append(bits)

        return image_invert