import os


from setuptools import find_packages, setup
from glob import glob

package_name = 'tf2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/" + package_name + "/launch", glob(os.path.join("launch", "*.launch.py"))),
        ("share/" + package_name + "/urdf", glob(os.path.join("urdf", "*.*"))),
        ("share/" + package_name + "/rviz", glob(os.path.join("rviz", "*.*"))),
        ("share/" + package_name + "/meshes", glob(os.path.join("meshes", "*.*"))),

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
        'console_scripts': [
            "static_turtle_tf2_broadcaster = tf2.static_turtle_tf2_broadcaster:main",
            "dynamic_turtle_tf2_broadcaster = tf2.dynamic_turtle_tf2_broadcaster:main",
            "tf_listener = tf2.tf_listener:main",
            "turtle_tf_listener = tf2.turtle_tf_listener:main",
        ],
    },
)
