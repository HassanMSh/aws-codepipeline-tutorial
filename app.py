#!/usr/bin/env python3
import aws_cdk as cdk
from aws_codepipeline_tutorial.aws_codepipeline_tutorial_stack import AwsCodepipelineTutorialStack

app = cdk.App()
AwsCodepipelineTutorialStack(app, "AwsCodepipelineTutorialStack",
                             env=cdk.Environment(account="123456789012", region="us-east-1")
                                )

app.synth()
