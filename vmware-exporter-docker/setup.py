from setuptools import setup, find_packages
import vmware_exporter

setup(
    name='vmware_exporter',
    version=vmware_exporter.__version__,
    packages=find_packages(),
    package_data={p: ["*"] for p in find_packages()},
    url="",
    license="",
    author="",
    author_email="",
    description="",
    entry_points={
        'console_scripts': [
            'vmware_exporter=vmware_exporter.vmware_exporter:main'
        ]
    }
)