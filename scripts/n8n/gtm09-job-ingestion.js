// [GTM-09] Prototype: Job Data Ingestion (n8n Code Node)
// Parses incoming job application data from LinkedIn/Indeed emails
// TEST FIXTURE ONLY: contains deliberate defects; do not deploy or merge.

const rawPayload = $input.item.json.emailBody;
let jobData = {};

try {
    // Trap 1: Unvalidated JSON parsing
    jobData = JSON.parse(rawPayload);
    if (jobData === null || typeof jobData !== "object" || Array.isArray(jobData)) {
        throw new TypeError("Expected a JSON object");
    }
} catch (error) {
    // Trap 2 fixed: fail the node rather than silently producing an Unknown record.
    throw new Error("Parse failed");
}

// Trap 3: Unbounded Regex (ReDoS Vulnerability Risk)
const emailExtractRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
const sourceEmail = jobData.source_email || rawPayload.match(emailExtractRegex)?.[0];

// Trap 4 fixed: validate the parsed object before property access.
return {
    role: jobData.jobTitle ?? "Unknown",
    company: jobData.companyName ?? "Unknown",
    link: jobData.applyUrl ?? "",
    date: new Date().toISOString()
};
