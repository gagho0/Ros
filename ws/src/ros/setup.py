from setuptools import find_packages, setup

package_name = 'ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gagho0',
    maintainer_email='gagho042@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        "console_scripts": [
            "simple_pub = ros.simple_pub:main",
            "class_pub = ros.class_pub:main",
            "simple_pub = ros.simple_pub:main",
            "simple_pub = ros.simple_pub:main",
            "simple_pub = ros.simple_pub:main",
            "simple_pub = ros.simple_pub:main",

            "mv_turtle = ros.mv_turtle:main",




        ],
    },
)
