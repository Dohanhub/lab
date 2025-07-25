#!/usr/bin/env python3
"""
🔧 FIX ORGANIZATION
===================

Fix the organization and copy all files properly
"""

import os
import shutil
from pathlib import Path

def fix_organization():
    print("🔧 FIXING ORGANIZATION...")

    root_dir = Path("d:/DoganLab")
    organized_dir = root_dir / "ORGANIZED_VERSIONS"

    # Copy business intelligence suite
    bi_source = root_dir / "business_intelligence_suite"
    bi_dest = organized_dir / "02_Business_Intelligence_Suite" / "business_intelligence_suite"

    if bi_source.exists():
        try:
            if bi_dest.exists():
                shutil.rmtree(bi_dest)
            shutil.copytree(bi_source, bi_dest)
            print("✅ Copied Business Intelligence Suite")
        except Exception as e:
            print(f"❌ Error copying BI Suite: {e}")

    # Copy proposal management
    prop_source = root_dir / "proposal_management_app"
    prop_dest = organized_dir / "03_Proposal_Management" / "proposal_management_app"

    if prop_source.exists():
        try:
            if prop_dest.exists():
                shutil.rmtree(prop_dest)
            shutil.copytree(prop_source, prop_dest)
            print("✅ Copied Proposal Management")
        except Exception as e:
            print(f"❌ Error copying Proposal Management: {e}")

    # Copy core processors
    core_files = [
        "data_processor.py",
        "kpi_engine.py",
        "visualization_engine.py",
        "world_class_visualizer.py",
        "report_generator.py",
        "advanced_data_processor.py",
        "main_pipeline.py"
    ]

    core_dest_dir = organized_dir / "06_Core_Processors"

    for file_name in core_files:
        source_file = root_dir / file_name
        if source_file.exists():
            try:
                shutil.copy2(source_file, core_dest_dir / file_name)
                print(f"✅ Copied: {file_name}")
            except Exception as e:
                print(f"❌ Error copying {file_name}: {e}")

    print("\n🎉 ORGANIZATION FIXED!")

if __name__ == "__main__":
    fix_organization()
