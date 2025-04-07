import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Slider } from "@/components/ui/slider";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from "@/components/ui/select";

export default function AdvancedAISettings() {
  const [advanced, setAdvanced] = useState(false);
  const [tone, setTone] = useState("neutral");
  const [creativity, setCreativity] = useState(50);
  const [format, setFormat] = useState("paragraph");
  const [basePrompt, setBasePrompt] = useState("");

  return (
    <div className="p-6 flex flex-col gap-6 max-w-3xl mx-auto">
      <Card>
        <CardContent className="p-6 space-y-4">
          <h2 className="text-xl font-semibold">AI Settings</h2>

          {/* Advanced Mode Toggle */}
          <label className="flex justify-between items-center">
            Advanced Mode
            <Switch checked={advanced} onCheckedChange={setAdvanced} />
          </label>

          {/* Base Prompt */}
          <label>
            Base Prompt
            <Textarea value={basePrompt} onChange={(e) => setBasePrompt(e.target.value)} />
          </label>

          {/* Communication Tone */}
          <label>
            Communication Tone
            <Select value={tone} onValueChange={setTone}>
              <SelectTrigger>
                <SelectValue placeholder="Select Tone" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="neutral">Neutral</SelectItem>
                <SelectItem value="formal">Formal</SelectItem>
                <SelectItem value="casual">Casual</SelectItem>
                <SelectItem value="humorous">Humorous</SelectItem>
              </SelectContent>
            </Select>
          </label>

          {/* Response Format */}
          <label>
            Response Format
            <Select value={format} onValueChange={setFormat}>
              <SelectTrigger>
                <SelectValue placeholder="Select Format" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="paragraph">Paragraph</SelectItem>
                <SelectItem value="bullets">Bullet Points</SelectItem>
                <SelectItem value="steps">Step-by-Step</SelectItem>
              </SelectContent>
            </Select>
          </label>

          {/* Creativity Slider */}
          <label>
            Creativity
            <Slider value={creativity} onValueChange={setCreativity} min={0} max={100} />
          </label>

          {/* Advanced Settings Section */}
          {advanced && (
            <div className="space-y-4 border-t pt-4">
              <h3 className="text-lg font-semibold">Advanced Settings</h3>
              <label>
                Custom Parameters (JSON Format)
                <Textarea placeholder='{"temperature": 0.7, "max_tokens": 150}' />
              </label>
              <Button variant="outline">Auto-Tune</Button>
            </div>
          )}

          <Button className="w-full mt-4">Apply Settings</Button>
        </CardContent>
      </Card>
    </div>
  );
}
