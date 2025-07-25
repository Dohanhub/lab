# ?? AFCO Automatic Document Processing System

?? **In Loving Memory of Omar (2007-2024)**
*"Forever 17, Forever Inspiring Innovation"*

## ?? **Quick Start**

### **1. Launch the System**
```cmd
LAUNCH_AUTO_DOCUMENT_SYSTEM.bat
```

### **2. Open Your Browser**
Navigate to: `http://localhost:8503`

### **3. Start Processing**
- Add folders to monitor
- Configure field mappings
- Watch automatic processing in real-time

---

## ?? **Key Features**

### **?? Automatic Folder Monitoring**
- **Real-time file detection** - Monitors folders for new documents
- **Multi-format support** - Excel, Word, PDF, CSV processing
- **Automatic processing** - No manual intervention required
- **Saudi market optimization** - Arabic text and SAR currency support

### **??? Smart Field Mapping**
- **AI-powered mapping** - Automatic field detection and mapping
- **Visual mapping interface** - Drag-and-drop field configuration
- **Custom transformation rules** - Clean and format data automatically
- **Validation rules** - Ensure data quality and consistency

### **?? Real-time Processing Analytics**
- **Live processing status** - Monitor file processing in real-time
- **Success/failure tracking** - Detailed processing history
- **Performance metrics** - Processing speed and accuracy stats
- **Visual dashboards** - Charts and graphs for insights

### **?? Advanced Configuration**
- **Flexible processing rules** - Customize extraction logic
- **Multiple folder monitoring** - Watch unlimited folders simultaneously
- **Automatic SQL generation** - Ready-to-use database scripts
- **Comprehensive logging** - Full audit trail of all activities

---

## ?? **System Requirements**

### **Software Requirements**
- Windows 10/11 or Linux
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 1GB free disk space

### **Supported File Formats**
- **Excel**: `.xlsx`, `.xls`
- **Word**: `.docx`, `.doc`
- **PDF**: `.pdf` (with table extraction)
- **CSV**: `.csv` (with encoding detection)

### **Database Support**
- SQLite (built-in)
- Production database integration ready

---

## ?? **Installation & Setup**

### **Automatic Installation**
1. Run `LAUNCH_AUTO_DOCUMENT_SYSTEM.bat`
2. System will install dependencies automatically
3. Follow the on-screen instructions

### **Manual Installation**
```cmd
# Install Python dependencies
pip install -r requirements.txt

# Create data directories
mkdir data\auto_watch data\processed data\mappings data\extractions data\sql_exports

# Start the system
streamlit run document_upload_interface.py --server.port=8503
```

---

## ?? **User Guide**

### **1. Folder Monitor Tab**
- **Add Watch Folders**: Enter folder paths to monitor
- **Real-time Status**: See active monitoring status
- **Recent Activity**: View latest processed files

### **2. File Manager Tab**
- **Browse Files**: View all files in monitored folders
- **Filter Options**: Filter by type, status, date
- **Bulk Actions**: Process multiple files at once
- **File Details**: Detailed information and actions

### **3. Field Mapping Tab**
- **Create Mappings**: Define source-to-target field mappings
- **Current Mappings**: View and edit existing mappings
- **AI Suggestions**: Get smart mapping recommendations

### **4. Processing Status Tab**
- **Real-time Metrics**: Success rates, processing times
- **Timeline Charts**: Visual processing history
- **Export Reports**: Download processing reports

### **5. Configuration Tab**
- **Processing Rules**: Configure data extraction rules
- **Folder Settings**: Set up monitoring preferences
- **Advanced Options**: System-level configurations

---

## ?? **Saudi Market Features**

### **Arabic Language Support**
- **RTL Text Handling** - Proper Arabic text processing
- **Bilingual Field Names** - Support for Arabic/English field names
- **Character Encoding** - Automatic encoding detection (UTF-8, CP1256)

### **Saudi Business Intelligence**
- **Company Detection** - Automatic recognition of Saudi companies
- **SAR Currency Processing** - Saudi Riyal amount extraction
- **Phone Number Formatting** - Saudi phone number standards (+966, 05)
- **Compliance Validation** - Saudi market regulation checks

### **Pre-configured Mappings**
```yaml
# Example Saudi market mappings
Company Name ? clients.name
??? ?????? ? clients.name_ar
Sector ? clients.sector
Contact Person ? clients.contact_person
Phone ? clients.phone (auto-format for +966)
Amount SAR ? financial_transactions.amount_sar
```

---

## ?? **Workflow Examples**

### **Client Data Processing**
1. **File Detection**: Excel file with client data appears in watch folder
2. **Automatic Extraction**: System extracts company names, contacts, sectors
3. **Field Mapping**: Maps to `clients` table fields automatically
4. **Validation**: Checks email formats, phone numbers, required fields
5. **SQL Generation**: Creates INSERT statements for database
6. **Storage**: Saves processed data and generates audit trail

### **RFQ Document Processing**
1. **PDF Detection**: RFQ document uploaded to watch folder
2. **Table Extraction**: Extracts tables and structured data from PDF
3. **Entity Recognition**: Identifies RFQ titles, values, deadlines
4. **Saudi Market Analysis**: Detects Arabic content and SAR amounts
5. **Mapping**: Maps to `rfqs` table with proper field assignments
6. **Output**: Generates SQL scripts and processing reports

---

## ?? **Configuration Examples**

### **Watch Folder Setup**
```yaml
# Add multiple folders for monitoring
watch_folders:
  - "D:\\Documents\\AFCO\\Incoming"
  - "\\\\server\\shared\\RFQs"
  - "C:\\Users\\Public\\Documents\\ClientData"
```

### **Field Mapping Configuration**
```yaml
# Custom field mappings
field_mappings:
  "Company Name": "clients.name"
  "??? ??????": "clients.name_ar"
  "Email Address": "clients.email"
  "RFQ Value": "rfqs.value_sar"
  "????? ???????": "rfqs.deadline"
```

### **Processing Rules**
```yaml
# Custom extraction rules
extraction_rules:
  saudi_companies:
    patterns: ["aramco", "sabic", "stc", "????"]
    target_table: "clients"
    priority: 10

  financial_amounts:
    patterns: ["sar", "????", "amount", "????"]
    target_table: "financial_transactions"
    priority: 8
```

---

## ??? **Troubleshooting**

### **Common Issues**

**? "Folder not found" error**
- Check folder path exists and is accessible
- Ensure proper permissions for folder access
- Use full absolute paths (e.g., `D:\Documents\AFCO`)

**? "No data extracted" warning**
- Verify file format is supported
- Check if file contains structured data (tables)
- Ensure file is not password protected or corrupted

**? "Field mapping failed" error**
- Review field mapping configuration
- Check source field names match document headers
- Verify target table and field names are correct

### **Performance Optimization**

**?? Speed up processing:**
- Reduce `processing_delay_seconds` in config
- Increase `max_concurrent_processing` (within system limits)
- Use smaller file sizes when possible
- Enable SSD storage for data directories

**?? Memory optimization:**
- Lower `max_memory_usage_mb` in config
- Process files in smaller batches
- Clear processing history regularly
- Restart system if memory usage is high

---

## ?? **Security & Privacy**

### **Data Protection**
- All processing happens locally - no cloud uploads
- Sensitive data never leaves your system
- Optional encryption for processed data
- Comprehensive audit trails

### **Access Control**
- Folder-level permissions respected
- Processing logs for compliance
- Secure file handling protocols
- No external network access required

---

## ?? **Support & Resources**

### **Documentation**
- **User Manual**: Complete guide with screenshots
- **API Reference**: For developers and integration
- **Configuration Guide**: Advanced setup instructions
- **Best Practices**: Optimization tips and guidelines

### **Getting Help**
- Check this README for common solutions
- Review system logs in `data/auto_processing.log`
- Use the built-in help system in the web interface
- Contact system administrator for advanced support

---

## ?? **Omar's Legacy**

This system is dedicated to the memory of Omar (2007-2024), whose vision of seamless document processing and intelligent automation continues to inspire innovation. Every feature is built with his memory in mind, ensuring his legacy of excellence and dedication to technological advancement lives on.

**"Forever 17, Forever Inspiring Innovation"**

---

## ?? **Future Enhancements**

### **Planned Features**
- **Voice Commands** - Process files using voice instructions
- **Mobile App** - Monitor processing from mobile devices
- **Advanced AI** - Machine learning for better field detection
- **Cloud Integration** - Optional cloud storage and processing
- **Workflow Automation** - Custom business process automation

### **Integration Roadmap**
- **ERP Systems** - Direct integration with SAP, Oracle
- **CRM Platforms** - Salesforce, Dynamics 365 connectivity
- **Document Management** - SharePoint, OneDrive integration
- **Business Intelligence** - Power BI, Tableau dashboard creation

---

**?? Ready to revolutionize your document processing workflow!**

*Built with ?? in memory of Omar - transforming business intelligence through innovation*
