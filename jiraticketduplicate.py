tickets=[{
        "summary": "Investigate %Active Metric test case breakdown in trend visualization",
        "description": "The %Active metric in the trend chart visualization fails due to misalignment in formula logic. This requires a root cause analysis and test stabilization.",
        "labels": ["tc-failure", "trendchart"],
        "components": ["TrendChart"],
        "issuetype": "Task",
        "epic": "STF-21"
    },
    {
        "summary": "Resolve test failures for trend chart %Active metric logic",
        "description": "Test executions for the %Active metric display incorrect outputs in trend charts. Suspected cause is logic inconsistency. Fix is needed urgently.",
        "labels": ["metric-type", "bugfix"],
        "components": ["TrendChart"],
        "issuetype": "Bug",
        "epic": "STF-21"
    },
    {
        "summary": "Stabilize trend chart TC results for %Active computation",
        "description": "The current test coverage for %Active metric on trend charts is failing intermittently. Investigation into formula correctness is required.",
        "labels": ["metric-type", "tc-failure"],
        "components": ["TrendChart"],
        "issuetype": "Story",
        "epic": "STF-21"
    },
    {
        "summary": "Diagnose failure in %Active trend test validations",
        "description": "Validation errors are observed in test cases concerning %Active metric rendering within the trend chart. The formula used might be causing the deviation.",
        "labels": ["tc-failure", "validation"],
        "components": ["TrendChart"],
        "issuetype": "Task",
        "epic": "STF-21"
    },
    {

        "summary": "Enable metric creation from event setup UI",
        "description": "Users should be able to define new stock and %active metrics while configuring events using the frontend interface.",
        "labels": ["frontend", "metric-creation"],
        "components": ["UI"],
        "issuetype": "Task",
        "epic": "STF-23"
    },
    {
        "summary": "Support UI-based input for %active and stock metrics",
        "description": "Introduce frontend input controls to allow dynamic entry of %active and stock metrics during event setup.",
        "labels": ["metric-creation", "ux"],
        "components": ["UI"],
        "issuetype": "Story",
        "epic": "STF-23"
    },
    {
        "summary": "Add frontend support to configure stock metrics in events",
        "description": "The frontend UI should support setting stock and %active metrics as part of the event configuration process.",
        "labels": ["frontend", "stock-metric"],
        "components": ["UI"],
        "issuetype": "Bug",
        "epic": "STF-23"
    },
    {
        "summary": "UI support for creating new metrics at event design time",
        "description": "Allow event designers to define stock/%active metrics in the UI without requiring backend input.",
        "labels": ["metric-creation", "frontend"],
        "components": ["UI"],
        "issuetype": "Story",
        "epic": "STF-23"
    },
{
    "summary": "Support MySQL integration for regression runs in MetricUploader",
    "description": "MetricUploader needs MySQL connectivity to properly handle test data during regression cycles.",
    "labels": [
      "mysql",
      "regression"
    ],
    "components": [
      "Database"
    ],
    "issuetype": "Story",
    "epic": "STF-22"
  },
  {
    "summary": "Add backend MySQL support in regression path",
    "description": "Ensure that the backend system supports MySQL interactions when executing regression test flows.",
    "labels": [
      "backend",
      "mysql"
    ],
    "components": [
      "Database"
    ],
    "issuetype": "Bug",
    "epic": "STF-22"
  },
  {
    "summary": "Implement regression support for MySQL in metric pipeline",
    "description": "Enable support for MySQL database during metric regression processes through MetricUploader.",
    "labels": [
      "regression",
      "metrics"
    ],
    "components": [
      "Database"
    ],
    "issuetype": "Task",
    "epic": "STF-22"
  },
  {
    "summary": "Enable MySQL in backend tests for metric data upload",
    "description": "Activate and test MySQL functionality for MetricUploader backend during regression runs.",
    "labels": [
      "mysql",
      "backend"
    ],
    "components": [
      "Database"
    ],
    "issuetype": "Task",
    "epic": "STF-22"
  },
{
    "summary": "Use Redis to speed up backend result fetching",
    "description": "Integrate Redis cache to accelerate retrieval of heavy backend output data.",
    "labels": [
      "redis",
      "caching"
    ],
    "components": [
      "Backend"
    ],
    "issuetype": "Story",
    "epic": "STF-22"
  },
  {
    "summary": "Backend optimization using Redis for large data queries",
    "description": "Optimize backend performance by caching large result sets in Redis.",
    "labels": [
      "performance",
      "redis"
    ],
    "components": [
      "Backend"
    ],
    "issuetype": "Task",
    "epic": "STF-22"
  },
  {
    "summary": "Add Redis cache layer to reduce query latency",
    "description": "Leverage Redis as a caching layer to improve response time when accessing output datasets.",
    "labels": [
      "backend",
      "redis"
    ],
    "components": [
      "Backend"
    ],
    "issuetype": "Bug",
    "epic": "STF-22"
  },
  {
    "summary": "Enable output caching in Redis for faster loads",
    "description": "Store computed backend results in Redis to improve subsequent fetch performance.",
    "labels": [
      "performance",
      "backend"
    ],
    "components": [
      "Backend"
    ],
    "issuetype": "Task",
    "epic": "STF-22"
  },
  {
    "summary": "Refactor RG, DS, TC, CG, and GVA modules to reduce processing time",
    "description": "Execution times across multiple modules including Result Grid, Driver Summary, Test Cases, CG pipeline, and GVA screen are high. Code-level refactoring and optimization are needed to improve throughput.",
    "labels": [
      "performance",
      "refactoring",
        "optimization"
    ],
    "components": [
      "MetricEngine"
    ],
    "issuetype": "Story",
    "epic": "STF-21"
  },
  {
    "summary": "Improve system speed by optimizing critical RG/DS/TC/CG/GVA flows",
    "description": "The existing implementations for key flows like RG, DS, TC, CG, and GVA are causing performance lags. Optimize and re-engineer bottlenecks for faster runtime behavior.",
    "labels": [
      "performance",
      "optimization"
    ],
    "components": [
      "MetricEngine"
    ],
    "issuetype": "Task",
    "epic": "STF-21"
  },
  {
    "summary": "Rework performance-heavy areas in RG, DS, TC, CG, and GVA",
    "description": "Certain parts of the RG, DS, TC, CG, and GVA modules are resource-intensive. Target these areas for cleanup and improved algorithm efficiency.",
    "labels": [
      "performance",
      "optimization"
    ],
    "components": [
      "MetricEngine"
    ],
    "issuetype": "Bug",
    "epic": "STF-21"
  },
  {
    "summary": "Optimize backend logic in RG, DS, TC, CG, and GVA for better performance",
    "description": "Backend computations for the listed modules need tuning to ensure scalability and responsiveness under load. Apply best practices in code and DB access to address bottlenecks.",
    "labels": [
      "performance",
      "optimization"
    ],
    "components": [
      "MetricEngine"
    ],
    "issuetype": "Bug",
    "epic": "STF-21"
  },
 {
    "summary": "Build interface for selecting metrics and attributes during event setup",
    "description": "Design and implement a frontend screen to allow users to choose relevant metrics and attributes when configuring events.",
    "labels": ["ui", "event-config"],
    "components": ["Frontend"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
  {
    "summary": "Develop form-based UI for event metric configuration",
    "description": "Introduce a structured form on the frontend for configuring which metrics and attributes are associated with an event.",
    "labels": ["ui", "event-setup"],
    "components": ["Frontend"],
    "issuetype": "Task",
    "epic": "STF-23"
  },
  {
    "summary": "Enable dynamic metric selection interface in event creation flow",
    "description": "Frontend should support dynamic UI controls that allow users to select metrics and attributes during event setup.",
    "labels": ["frontend", "metric-selection"],
    "components": ["Frontend"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
  {
    "summary": "Implement dropdown-based UI for event metrics",
    "description": "Provide a user-friendly dropdown interface to select attributes and metrics while setting up a new event.",
    "labels": ["ui", "dropdown"],
    "components": ["Frontend"],
    "issuetype": "Bug",
    "epic": "STF-23"
  },
{
    "summary": "Provision SEQ setup for validating Redis cache functionality",
    "description": "Set up the SEQ environment specifically to assess Redis cache behavior and ensure system compatibility.",
    "labels": ["redis", "seq"],
    "components": ["CacheLayer"],
    "issuetype": "Story",
    "epic": "STF-22"
  },
  {
    "summary": "Create testbed for Redis integration using SEQ environment",
    "description": "Build a dedicated SEQ-based testbed to simulate Redis caching under real-world conditions and assess stability.",
    "labels": ["seq", "redis-test"],
    "components": ["CacheLayer"],
    "issuetype": "Bug",
    "epic": "STF-22"
  },
  {
    "summary": "Setup Redis load testing environment using SEQ",
    "description": "Prepare SEQ infrastructure to evaluate Redis under load and monitor caching response times.",
    "labels": ["performance", "seq"],
    "components": ["CacheLayer"],
    "issuetype": "Task",
    "epic": "STF-22"
  },
  {
    "summary": "Establish SEQ stack for Redis integration testing",
    "description": "Deploy SEQ stack to validate Redis caching layers for consistent integration and performance under scale.",
    "labels": ["redis", "integration", "seq"],
    "components": ["CacheLayer"],
    "issuetype": "Story",
    "epic": "STF-22"
  },
 {
    "summary": "Enable versioned analysis configurations within events",
    "description": "Introduce support for version-controlled analysis settings to ensure that each event can store multiple output configurations.",
    "labels": ["analysis", "config-versioning"],
    "components": ["Versioning"],
    "issuetype": "Task",
    "epic": "STF-24"
  },
  {
    "summary": "Support multiple analysis setting versions per event",
    "description": "Allow events to maintain different versions of analysis settings, enabling users to switch or compare output results.",
    "labels": ["versioning", "analysis"],
    "components": ["Versioning"],
    "issuetype": "Story",
    "epic": "STF-24"
  },
  {
    "summary": "Implement output segmentation by analysis config version",
    "description": "Each analysis setting version should generate and retain separate output datasets for better audit and comparison.",
    "labels": ["versioning", "segmentation"],
    "components": ["Versioning"],
    "issuetype": "Bug",
    "epic": "STF-24"
  },
  {
    "summary": "Introduce independent analysis version control inside events",
    "description": "Design versioning logic for analysis parameters so users can manage configuration changes across event lifecycles.",
    "labels": ["analysis", "audit"],
    "components": ["Versioning"],
    "issuetype": "Story",
    "epic": "STF-24"
  },
 {
    "summary": "Enable role-based permissions to access events",
    "description": "Implement fine-grained access control for events based on user roles. Users should only be able to view, edit, or delete events depending on their assigned role (e.g., viewer, editor, admin). This includes enforcing backend-level checks and updating the UI accordingly to reflect restricted actions.",
    "labels": ["permissions", "event"],
    "components": ["EventSetup"],
    "issuetype": "Story",
    "epic": "STF-24"
  },
  {
    "summary": "Control event visibility and modification using roles",
    "description": "Add support to manage event visibility and modification rights through role-based controls. This should support granular restrictions ensuring unauthorized roles cannot perform sensitive changes.",
    "labels": ["event", "history","permission"],
    "components": ["EventSetup"],
    "issuetype": "Bug",
    "epic": "STF-24"
  },
  {
    "summary": "Implement RBAC for event-level permissions",
    "description": "Integrate Role-Based Access Control (RBAC) for event access within the platform. Users with different roles (e.g., contributor, admin) should have varying privileges for accessing and modifying events. Enforce this via middleware and UI gating.",
    "labels": ["audit", "event","permission"],
    "components": ["EventSetup"],
    "issuetype": "Task",
    "epic": "STF-24"
  },
  {
    "summary": "Add permission layers to event actions based on roles",
    "description": "Introduce role-sensitive access layers to event-level operations such as edit, delete, and share. Role definitions should dictate what actions are visible and executable to the user at both frontend and backend.",
    "labels": ["versioning", "traceability","permission"],
    "components": ["EventSetup"],
    "issuetype": "Story",
    "epic": "STF-24"
  },
   {
    "summary": "Fix layout issues in GVA view for major browsers",
    "description": "The Group Value Attribute screen suffers from alignment problems across Chrome and Firefox. Needs CSS adjustments for consistent layout.",
    "labels": ["gva", "layout"],
    "components": ["UX"],
    "issuetype": "Bug",
    "epic": "STF-23"
  },
  {
    "summary": "Correct UI displacement on GVA group screen",
    "description": "UI components in the GVA group screen are not aligning properly in different browsers. Require frontend fixes for stable rendering.",
    "labels": ["ux", "cross-browser"],
    "components": ["UX"],
    "issuetype": "Task",
    "epic": "STF-23"
  },
  {
    "summary": "Investigate misaligned elements in GVA interface",
    "description": "On the GVA screen, layout inconsistencies appear when switching between Chrome and Firefox. Diagnose and adjust frontend elements accordingly.",
    "labels": ["gva", "frontend"],
    "components": ["UX"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
  {
    "summary": "Browser-specific alignment issue in group value UI",
    "description": "Group screen UI is rendered differently in Firefox compared to Chrome. Address spacing and positioning bugs to unify behavior.",
    "labels": ["ux", "compatibility"],
    "components": ["UX"],
    "issuetype": "Bug",
    "epic": "STF-23"
  },
    {
        "summary": "Build Driver Summary logic for stock-based metrics",
        "description": "Construct DS capabilities focused on stock attributes and ensure correct output generation for all event variations.",
        "labels": ["driver-summary", "stock-metric"],
        "components": ["DS"],
        "issuetype": "Story",
        "epic": "STF-25"
    },
    {
        "summary": "Implement stock metrics support in DS computation",
        "description": "Enable DS module to calculate and handle stock-related metrics across various event types. Validate correctness and consistency.",
        "labels": ["ds", "event-metrics"],
        "components": ["DS"],
        "issuetype": "Task",
        "epic": "STF-25"
    },
    {
        "summary": "Extend DS engine to process stock metrics",
        "description": "Enhance Driver Summary logic to include stock metric categories and run integration tests for end-to-end verification.",
        "labels": ["ds", "integration"],
        "components": ["DS"],
        "issuetype": "Bug",
        "epic": "STF-25"
    },
    {
        "summary": "Support stock metric calculations in Driver Summary",
        "description": "Driver Summary should now accept and correctly calculate stock-related metrics used during analysis workflows.",
        "labels": ["stock-metric", "ds"],
        "components": ["DS"],
        "issuetype": "Story",
        "epic": "STF-25"
    },
   {
    "summary": "Resolve timeout issues in model upload jobs",
    "description": "Timeouts are frequently encountered when uploading adhoc data for model application. Needs improvement in handling large requests.",
    "labels": ["model", "upload"],
    "components": ["Upload"],
    "issuetype": "Bug",
    "epic": "STF-25"
  },
  {
    "summary": "Handle delays in model execution on adhoc inputs",
    "description": "When adhoc datasets are uploaded, model processing is delayed and sometimes fails. Implement proper timeout and retry strategy.",
    "labels": ["adhoc", "timeout"],
    "components": ["Upload"],
    "issuetype": "Task",
    "epic": "STF-25"
  },
  {
    "summary": "Add retry mechanism for model run on large adhoc uploads",
    "description": "Model application fails for large adhoc uploads due to timeouts. Introduce retry logic and better job scheduling.",
    "labels": ["model", "retry"],
    "components": ["Upload"],
    "issuetype": "Story",
    "epic": "STF-25"
  },
  {
    "summary": "Prevent model timeout during on-demand uploads",
    "description": "On-demand data uploads for model execution often timeout. Introduce batching and timeout tolerance improvements.",
    "labels": ["timeout", "model-execution"],
    "components": ["Upload"],
    "issuetype": "Bug",
    "epic": "STF-25"
  },
   {
    "summary": "Block unauthorized edits to event headers by private users",
    "description": "Ensure private users cannot modify event headers by enforcing strict access control in the permissioning module.",
    "labels": ["security", "access-control"],
    "components": ["UserAccess"],
    "issuetype": "Bug",
    "epic": "STF-24"
  },
  {
    "summary": "Prevent event header modification by restricted users",
    "description": "Users with private access should be restricted from editing event headers. Apply permission checks to enforce this.",
    "labels": ["permissioning", "user-access"],
    "components": ["UserAccess"],
    "issuetype": "Task",
    "epic": "STF-24"
  },
  {
    "summary": "Ensure header edit rights are limited to authorized roles",
    "description": "Only specific roles should be allowed to update event headers. Update permissioning logic accordingly.",
    "labels": ["permission", "role-based-access"],
    "components": ["UserAccess"],
    "issuetype": "Story",
    "epic": "STF-24"
  },
  {
    "summary": "Patch for event header access control flaw",
    "description": "Fix access control bug that allows private users to edit event headers. Add permission validations.",
    "labels": ["security", "patch"],
    "components": ["UserAccess"],
    "issuetype": "Bug",
    "epic": "STF-24"
  },
   {
    "summary": "Create unified schema for customer data and event outputs in separate DBs",
    "description": "Build a unified schema to manage core entities like transactions, metrics, and customer attributes in a primary database. A secondary outputs database should handle processed results. Ensure performance tuning and modular schema design for growth.",
    "labels": ["database", "architecture"],
    "components": ["MetricEngine"],
    "issuetype": "Story",
    "epic": "STF-22"
  },
  {
    "summary": "Architect primary and secondary DB setup for platform-wide analytics",
    "description": "Design two-tiered database architecture: one primary DB for storing raw input data like metrics, attributes, and transactions, and one secondary DB dedicated to processed analytical results. Optimize for concurrency and data separation.",
    "labels":  ["database", "architecture"],
    "components": ["MetricEngine"],
    "issuetype": "Task",
    "epic": "STF-22"
  },
  {
    "summary": "Separate input data and output metrics into distinct scalable DBs",
    "description": "Refactor current data architecture to store transactional and metric input data in a centralized database, while keeping output result sets in an isolated DB for scalability and query efficiency. Apply best practices for partitioning and access control.",
    "labels": ["database", "architecture"],
    "components": ["MetricEngine"],
    "issuetype": "Story",
    "epic": "STF-22"
  },
  {
    "summary": "Design dual-DB system for inputs vs outputs to improve performance",
    "description": "Implement a dual-database structure: one for core inputs such as customer attributes and metrics, and another for outputs like analysis and segmentation results. Improve load distribution and make the system future-ready.",
    "labels": ["database", "architecture"],
    "components": ["MetricEngine"],
    "issuetype": "Task",
    "epic": "STF-22"
  },
   {
        "summary": "Dockerize task server for Linux-based environments",
        "description": "Create Docker containers for the task server to allow seamless deployment across Linux machines.",
        "labels": ["containerization", "docker"],
        "components": ["Deployment"],
        "issuetype": "Task",
        "epic": "STF-22"
    },
    {
        "summary": "Enable container support for task server on Linux",
        "description": "Ensure that the task server is packaged as a container for compatibility with Linux VM deployments.",
        "labels": ["linux", "containerization"],
        "components": ["Deployment"],
        "issuetype": "Story",
        "epic": "STF-22"
    },
    {
        "summary": "Prepare task server image for Linux VM deployment",
        "description": "Build and test a container image of the task server optimized for Linux VM hosting.",
        "labels": ["deployment", "linux"],
        "components": ["Deployment"],
        "issuetype": "Bug",
        "epic": "STF-22"
    },
    {
        "summary": "Support task server container rollout on Linux infrastructure",
        "description": "Containerize the task server and verify its deployment on Linux-based cloud or on-prem VMs.",
        "labels": ["scalable", "containerization"],
        "components": ["Deployment"],
        "issuetype": "Story",
        "epic": "STF-22"
    },
   {
    "summary": "Develop grid view to display segmentation results",
    "description": "Implement a result grid that presents customer segmentation outcomes by key dimensions.",
    "labels": ["segmentation", "result-grid"],
    "components": ["ResultGrid"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
  {
    "summary": "Create UI component for segmented customer data",
    "description": "Design a user interface grid to organize and show customer segments clearly.",
    "labels": ["segmentation", "ui"],
    "components": ["ResultGrid"],
    "issuetype": "Task",
    "epic": "STF-23"
  },
  {
    "summary": "Render tabular view for segmentation analysis output",
    "description": "Provide a structured table to present the output of segmentation analysis for end users.",
    "labels": ["segmentation", "table-view"],
    "components": ["ResultGrid"],
    "issuetype": "Bug",
    "epic": "STF-23"
  },
  {
    "summary": "Expose grouped segmentation results in frontend grid",
    "description": "Enable frontend view to group segmentation results based on customer characteristics.",
    "labels": ["segmentation", "frontend"],
    "components": ["ResultGrid"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
   {
    "summary": "Develop UI functionality to upload customer attributes",
    "description": "Provide a user interface that allows uploading new customer attributes with proper field validations.",
    "labels": ["attribute", "upload"],
    "components": ["AttributeUploader"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
  {
    "summary": "Enable attribute input through frontend module",
    "description": "Allow users to input new customer attributes via frontend, enforcing validation checks.",
    "labels": ["attribute", "frontend"],
    "components": ["AttributeUploader"],
    "issuetype": "Task",
    "epic": "STF-23"
  },
  {
    "summary": "Implement customer attribute form with upload option",
    "description": "Design and build a form to support creation and uploading of customer-specific attributes.",
    "labels": ["upload", "form"],
    "components": ["AttributeUploader"],
    "issuetype": "Bug",
    "epic": "STF-23"
  },
  {
    "summary": "Frontend support for creating new customer properties",
    "description": "Add frontend support to define and submit new customer properties with validation handling.",
    "labels": ["attribute", "ui"],
    "components": ["AttributeUploader"],
    "issuetype": "Story",
    "epic": "STF-23"
  },
      {
        "summary": "Tune MySQL performance for multi-million row datasets",
        "description": "Enhance database performance by optimizing MySQL configurations for handling millions of rows.",
        "labels": ["mysql", "scalability"],
        "components": ["Performance"],
        "issuetype": "Story",
        "epic": "STF-22"
    },
    {
        "summary": "Improve query efficiency for large-scale MySQL records",
        "description": "Rework SQL query structures to boost execution efficiency for databases containing over 4 million rows.",
        "labels": ["mysql", "query"],
        "components": ["Performance"],
        "issuetype": "Task",
        "epic": "STF-22"
    },
    {
        "summary": "Redesign MySQL schema to support customer data scaling",
        "description": "Adjust database schema and indexes to efficiently manage growing volumes of customer data in MySQL.",
        "labels": ["scalability", "mysql"],
        "components": ["Performance"],
        "issuetype": "Bug",
        "epic": "STF-22"
    },
    {
        "summary": "Optimize backend to support high-volume MySQL transactions",
        "description": "Refactor backend architecture for high-volume MySQL transaction support as customer records grow.",
        "labels": ["performance", "mysql"],
        "components": ["Performance"],
        "issuetype": "Story",
        "epic": "STF-22"
    }

]