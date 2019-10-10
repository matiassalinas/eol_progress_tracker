import setuptools

setuptools.setup(
    name="progress_tracker",
    version="0.0.1",
    author="Matias Salinas",
    author_email="matsalinas@uchile.cl",
    description="Progress Tracker EOL LMS",
    long_description="Progress Tracker EOL LMS",
    url="https://eol.uchile.cl/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": [
            "progress_tracker = progress_tracker.apps:ProgressTrackerConfig",
        ],
    },
)
