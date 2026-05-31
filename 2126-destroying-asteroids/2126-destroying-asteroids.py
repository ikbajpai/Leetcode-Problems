class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        planet_mass = mass
        asteroids.sort()

        for i in range(len(asteroids)):
            if planet_mass>=asteroids[i]:
                planet_mass+=asteroids[i]
            else:
                return False
        return True        