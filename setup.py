from setuptools import setup

package_name = 'send_list'
submodules = 'send_list/make_list'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uchida',
    maintainer_email='uchida@todo.todo',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = send_list.publisher_member_function:main',
            'listener = send_list.subscriber_member_function:main',
            'stepping_move = send_list.subscriber_stepping_move:main',
            'sub_servo = send_list.subscriber_servomotor_move:main',
        ],
    },
)
