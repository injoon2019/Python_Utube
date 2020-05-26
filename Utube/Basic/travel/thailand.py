class ThailandPackage:
    def detail(self):
        print("Thai Package 3/4")

if __name__ == "__main__":
    print("Thailand module directly")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Call from other side not Thai")
