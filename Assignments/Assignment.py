import cv2 as cv
import numpy as np
import os 
import matplotlib.pyplot as plt     

class ImagePipeline:  
    def __init__(self, folder):
        self.folder = folder
        self.images = []
        self.gray_images = []
        self.results = []
        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def load_images(self):
        for file in os.listdir(self.folder):
            if file.endswith(".jpg"):
                img = cv.imread(os.path.join(self.folder, file))
                if img is not None:
                    self.images.append((file, img))

    def preprocess(self):
        for name, img in self.images:
            img = cv.resize(img, (512, 512))
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (5, 5), 0)
            self.gray_images.append((name, gray))
            self.results.append((name, img, blur))

    def extract_features(self):
        for name, original, blur in self.results:
            edges = cv.Canny(blur, 100, 200)
            faces = self.face_cascade.detectMultiScale(blur, 1.1, 4)
            mean = np.mean(blur)
            contrast = np.std(blur)
            edge_density = np.sum(edges > 0) / edges.size
            self.results.append((name, mean, contrast, edge_density, len(faces)))

    def analyze(self):
        features = [(r[1], r[2], r[3]) for r in self.results if isinstance(r[1], float)]
        matrix = np.array(features)
        cov = np.cov(matrix, rowvar=False)
        eig_vals, _ = np.linalg.eig(cov)
        best = max(self.results, key=lambda x: x[3] if isinstance(x[3], float) else -1)

        print("Covariance Matrix:\n", cov)
        print("Eigenvalues:\n", eig_vals)
        print("Image with highest edge density:", best[0])

    def show_histograms(self):
        for name, gray in self.gray_images:
            plt.hist(gray.ravel(), bins=256, range=(0, 256))
            plt.title(f"Histogram - {name}")
            plt.xlabel("Pixel Intensity")
            plt.ylabel("Count")
            plt.show()

    def run(self):
        self.load_images()
        self.preprocess()
        self.extract_features()
        self.analyze()
        self.show_histograms()


pipeline = ImagePipeline(r"face.png")
pipeline.run()