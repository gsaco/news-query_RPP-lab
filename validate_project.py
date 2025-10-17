"""
Project Validation Script
Checks that all required components are in place
"""
import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_directory_exists(dirpath, description):
    """Check if a directory exists"""
    exists = os.path.isdir(dirpath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {dirpath}")
    return exists

def validate_requirements():
    """Validate requirements.txt has key dependencies"""
    print("\n" + "="*80)
    print("VALIDATING REQUIREMENTS")
    print("="*80)
    
    required_packages = [
        'feedparser',
        'sentence-transformers',
        'chromadb',
        'langchain',
        'tiktoken',
        'pandas',
        'jupyter'
    ]
    
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
        
        all_found = True
        for package in required_packages:
            # Check if package name appears at start of line (with optional whitespace)
            found = any(line.strip().startswith(package + '=') or 
                       line.strip().startswith(package + '<') or
                       line.strip().startswith(package + '>') or
                       line.strip() == package
                       for line in lines)
            if found:
                print(f"✅ {package} found in requirements.txt")
            else:
                print(f"❌ {package} NOT found in requirements.txt")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def main():
    print("="*80)
    print("NEWS RETRIEVAL SYSTEM - PROJECT VALIDATION")
    print("="*80)
    
    checks = []
    
    # Check directory structure
    print("\n📁 Checking Directory Structure...")
    checks.append(check_directory_exists('src', 'Source code directory'))
    checks.append(check_directory_exists('data', 'Data directory'))
    checks.append(check_directory_exists('notebooks', 'Notebooks directory'))
    checks.append(check_directory_exists('outputs', 'Outputs directory'))
    
    # Check source files
    print("\n📝 Checking Source Code Files...")
    checks.append(check_file_exists('src/__init__.py', 'Package init'))
    checks.append(check_file_exists('src/rss_loader.py', 'RSS Loader'))
    checks.append(check_file_exists('src/tokenizer.py', 'Tokenizer'))
    checks.append(check_file_exists('src/embeddings.py', 'Embeddings'))
    checks.append(check_file_exists('src/vector_store.py', 'Vector Store'))
    checks.append(check_file_exists('src/langchain_pipeline.py', 'LangChain Pipeline'))
    checks.append(check_file_exists('src/utils.py', 'Utils'))
    
    # Check notebooks
    print("\n📓 Checking Notebooks...")
    checks.append(check_file_exists('notebooks/news_retrieval_system.ipynb', 'Main Notebook'))
    
    # Check data files
    print("\n📊 Checking Data Files...")
    checks.append(check_file_exists('data/sample_rpp_news.json', 'Sample Data'))
    checks.append(check_file_exists('data/README.md', 'Data README'))
    
    # Check documentation
    print("\n📚 Checking Documentation...")
    checks.append(check_file_exists('README.md', 'Main README'))
    checks.append(check_file_exists('SETUP.md', 'Setup Guide'))
    checks.append(check_file_exists('requirements.txt', 'Requirements'))
    checks.append(check_file_exists('.gitignore', 'Git Ignore'))
    
    # Check test/example files
    print("\n🧪 Checking Test/Example Files...")
    checks.append(check_file_exists('test_modules.py', 'Test Script'))
    checks.append(check_file_exists('example_usage.py', 'Example Script'))
    
    # Validate requirements
    checks.append(validate_requirements())
    
    # Summary
    print("\n" + "="*80)
    print("VALIDATION SUMMARY")
    print("="*80)
    total = len(checks)
    passed = sum(checks)
    failed = total - passed
    
    print(f"Total Checks: {total}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    
    if failed == 0:
        print("\n🎉 ALL VALIDATIONS PASSED!")
        print("\n✅ Project is complete and ready for submission!")
        return 0
    else:
        print(f"\n⚠️  {failed} validation(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
