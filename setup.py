setup(
    name="Firefighter",
    version="0.0.1",
    description="Generate daily order",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/wwainkrk",
    author="Sebastian Warszawa",
    author_email="warsaw0902@gmail.com.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["firefighter_app"],
    include_package_data=True,
    entry_points={"console_scripts": ["Firefighter=code.app:main"]},
)
