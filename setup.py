import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="master_deploy",
    version="0.0.1",

    description="Deployment CDK for Master",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "master_deploy"},
    packages=setuptools.find_packages(where="master_deploy"),

    install_requires=[
        "aws-cdk.core",
        "aws_cdk.aws_iam",
        "aws_cdk.aws_ec2",
        "aws_cdk.aws_ecr",
        "aws_cdk.aws_ecs",
        "aws_cdk.aws_elasticloadbalancingv2",
        "aws_cdk.aws_logs",
        "aws_cdk.aws_route53",
        "aws_cdk.aws_route53_targets"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
