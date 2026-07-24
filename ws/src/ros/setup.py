import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
            ),
        (
            'share/' + package_name,
            ['package.xml']),
        (
            "share/" + package_name + "/launch", 
            glob(os.path.join(
                "launch", 
                "*.launch.py"
                )
                )
                ),


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
            "simple_sub = ros.simple_sub:main",
            "class_pub = ros.class_pub:main",
            "class_sub = ros.class_sub:main",

            "mv_turtle = ros.mv_turtle:main",
            "mv_turtle_ns = ros.mv_turtle_ns:main",


            "qos_test_pub = ros.qos_test_pub:main",
            "qos_test_sub = ros.qos_test_sub:main",

            "user_int_pub = ros.user_int_pub:main",
            "user_int_sub = ros.user_int_sub:main",

            "service_server = ros.service_server:main",
            "service_thread_server = ros.service_thread_server:main",
            "service_client = ros.service_client:main",

            "my_param = ros.my_param:main",
            "param_async = ros.param_async:main",

            "action_server = ros.action_server:main",
            "action_client = ros.action_client:main",
            "action_thread_server = ros.action_thread_server:main"

            

        ],
    },
)
